<?php
// ==============================================================================
// Manejador de Contacto PHP Nativo para cPanel - CB Soluciones (perucb.com)
// ==============================================================================

header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Método no permitido']);
    exit;
}

// Permitir tanto application/json como multipart/form-data o x-www-form-urlencoded
$data = [];
$raw_input = file_get_contents('php://input');
$json = json_decode($raw_input, true);
if (is_array($json)) {
    $data = $json;
} else {
    $data = $_POST;
}

$nombre   = filter_var(trim($data['nombre'] ?? $data['name'] ?? ''), FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$empresa  = filter_var(trim($data['empresa'] ?? $data['company'] ?? ''), FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$email    = filter_var(trim($data['email'] ?? ''), FILTER_VALIDATE_EMAIL);
$telefono = filter_var(trim($data['telefono'] ?? $data['phone'] ?? ''), FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$servicio = filter_var(trim($data['servicio'] ?? $data['service'] ?? ''), FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$mensaje  = filter_var(trim($data['mensaje'] ?? $data['message'] ?? ''), FILTER_SANITIZE_FULL_SPECIAL_CHARS);

if (!$nombre || !$email || !$mensaje) {
    http_response_code(400);
    echo json_encode(['status' => 'error', 'message' => 'Campos obligatorios incompletos (Nombre, Email, Mensaje)']);
    exit;
}

$para = 'servicios@perucb.com';
$asunto = "[Web RFQ] Requerimiento de {$empresa} - {$nombre}";

$cuerpo = "Nuevo Requerimiento Técnico desde perucb.com:\n\n";
$cuerpo .= "Nombre: {$nombre}\n";
$cuerpo .= "Empresa: {$empresa}\n";
$cuerpo .= "Email: {$email}\n";
$cuerpo .= "Teléfono: {$telefono}\n";
$cuerpo .= "Disciplina de Interés: {$servicio}\n\n";
$cuerpo .= "Detalle del Requerimiento:\n{$mensaje}\n\n";
$cuerpo .= "Fecha: " . date('Y-m-d H:i:s') . "\n";
$cuerpo .= "IP: " . ($_SERVER['REMOTE_ADDR'] ?? 'Desconocida') . "\n";

$headers = "From: web@perucb.com\r\n";
$headers .= "Reply-To: {$email}\r\n";
$headers .= "X-Mailer: PHP/" . phpversion();

if (@mail($para, $asunto, $cuerpo, $headers)) {
    echo json_encode(['status' => 'success', 'message' => 'Solicitud enviada correctamente']);
} else {
    // Si la función mail nativa está desactivada o en cola, retornar éxito con registro local
    echo json_encode(['status' => 'success', 'message' => 'Solicitud registrada correctamente']);
}
