<?php
/**
 * ETS-BZH — réception des demandes de rappel.
 *
 * Ce fichier est le point d'arrivée des formulaires du site. Il est volontaire-
 * ment sans dépendance : il fonctionne sur n'importe quel hébergement PHP, y
 * compris l'offre mutualisée d'Hostinger.
 *
 * À vérifier une fois en ligne :
 *   1. DESTINATAIRE reçoit bien les demandes (testez une fois le site publié) ;
 *   2. EXPEDITEUR utilise une adresse du domaine, sinon les messages partent en
 *      indésirables ;
 *   3. si l'hébergeur bloque mail(), remplacez l'envoi par un service SMTP.
 *
 * Réponse : JSON {"ok": true} ou {"ok": false, "erreur": "..."}.
 */

const DESTINATAIRE = 'contact@etablissement-breizh.fr';
const EXPEDITEUR   = 'site@etablissement-breizh.fr';   // doit appartenir au domaine
const MAX_PAR_IP   = 6;                                 // demandes / 10 minutes

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

function repondre($ok, $erreur = null, $code = 200) {
    http_response_code($code);
    echo json_encode($ok ? ['ok' => true] : ['ok' => false, 'erreur' => $erreur],
                     JSON_UNESCAPED_UNICODE);
    exit;
}

/** Retire tout ce qui permettrait d'injecter un en-tête de courriel. */
function propre($v, $max = 300) {
    $v = is_string($v) ? $v : '';
    $v = str_replace(["\r", "\n", "\0"], ' ', $v);
    $v = trim(preg_replace('/\s+/u', ' ', $v));
    return mb_substr($v, 0, $max);
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    repondre(false, 'Méthode non autorisée.', 405);
}

$brut = file_get_contents('php://input');
$d = json_decode($brut, true);
if (!is_array($d)) { $d = $_POST; }

// Piège à robots : le champ est invisible, un humain ne le remplit jamais.
// On renvoie un succès pour ne pas renseigner le robot sur son échec.
if (!empty($d['_gotcha'])) { repondre(true); }

$tel = propre($d['telephone'] ?? '', 40);
if (preg_match_all('/\d/', $tel) < 9) {
    repondre(false, 'Merci d’indiquer un numéro de téléphone valide.', 422);
}
$ville = propre($d['ville'] ?? '', 80);
if ($ville === '') {
    repondre(false, 'Merci d’indiquer votre commune.', 422);
}

// Limitation simple par adresse IP. Si le dossier temporaire n'est pas
// accessible en écriture, on laisse simplement passer la demande.
$ip = propre($_SERVER['REMOTE_ADDR'] ?? '', 45);
$journal = sys_get_temp_dir() . '/ets-bzh-' . md5($ip) . '.txt';
$recentes = [];
if (@is_readable($journal)) {
    $recentes = array_filter(explode(',', (string) @file_get_contents($journal)),
                             fn($t) => (int) $t > time() - 600);
}
if (count($recentes) >= MAX_PAR_IP) {
    repondre(false, 'Trop de demandes envoyées depuis cet appareil.', 429);
}
$recentes[] = time();
@file_put_contents($journal, implode(',', $recentes), LOCK_EX);

$libelles = [
    'nom' => 'Nom', 'telephone' => 'Téléphone', 'email' => 'E-mail',
    'ville' => 'Ville', 'departement' => 'Département',
    'prestation' => 'Type d’intervention', 'urgence' => 'Degré d’urgence',
    'message' => 'Message', 'page' => 'Page d’origine',
];

// sprintf('%-20s') compte les octets : « Téléphone » et « Département »
// seraient décalés. On aligne sur le nombre de caractères.
$lignes = [];
foreach ($libelles as $cle => $libelle) {
    $v = propre($d[$cle] ?? '', $cle === 'message' ? 2000 : 300);
    if ($v === '') { continue; }
    $remplissage = str_repeat(' ', max(0, 20 - mb_strlen($libelle)));
    $lignes[] = $libelle . $remplissage . ' : ' . $v;
}

$corps = "Nouvelle demande de rappel depuis le site ETS-BZH\n"
       . str_repeat('-', 58) . "\n\n"
       . implode("\n", $lignes) . "\n\n"
       . str_repeat('-', 58) . "\n"
       . 'Reçue le ' . date('d/m/Y à H:i') . "\n";

$sujet = 'Demande de rappel — ' . $tel . ' — ' . $ville;

$entetes = [
    'From: ETS-BZH <' . EXPEDITEUR . '>',
    'Content-Type: text/plain; charset=UTF-8',
    'X-Mailer: ETS-BZH',
];
$courriel = filter_var(propre($d['email'] ?? '', 200), FILTER_VALIDATE_EMAIL);
if ($courriel) { $entetes[] = 'Reply-To: ' . $courriel; }

$envoye = @mail(DESTINATAIRE, '=?UTF-8?B?' . base64_encode($sujet) . '?=',
                $corps, implode("\r\n", $entetes));

if (!$envoye) {
    repondre(false, 'L’envoi de votre demande a échoué.', 500);
}
repondre(true);
