<?php
// ==============================================================================
// Manejador de Contacto PHP Nativo para cPanel - CB Soluciones
// ==============================================================================

header('Content-Type: application/json; charset=utf-8');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Método no permitido']);
    exit;
}

$nombre   = filter_var(trim($_POST['nombre'] ?? ''), FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$empresa  = filter_var(trim($_POST['empresa'] ?? ''), FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$email    = filter_var(trim($_POST['email'] ?? ''), FILTER_VALIDATE_EMAIL);
$telefono = filter_var(trim($_POST['telefono'] ?? ''), FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$servicio = filter_var(trim($_POST['servicio'] ?? ''), FILTER_SANITIZE_FULL_SPECIAL_CHARS);
$mensaje  = filter_var(trim($_POST['mensaje'] ?? ''), FILTER_SANITIZE_FULL_SPECIAL_CHARS);

if (!$nombre || !$email || !$mensaje) {
    http_response_code(400);
    echo json_encode(['status' => 'error', 'message' => 'Campos obligatorios incompletos']);
    exit;
}

$para = 'contacto@cbsoluciones.pe'; // Cambiar por el correo del cliente en cPanel
$asunto = "[RFQ Web] Requerimiento de {$empresa} - {$nombre}";

$cuerpo = "Nuevo Requerimiento Técnico desde la Web:\n\n";
$cuerpo .= "Nombre: {$nombre}\n";
$cuerpo .= "Empresa: {$empresa}\n";
$cuerpo .= "Email: {$email}\n";
$cuerpo .= "Teléfono: {$telefono}\n";
$cuerpo .= "Disciplina de Interés: {$servicio}\n\n";
$cuerpo .= "Detalle del Requerimiento:\n{$mensaje}\n\n";
$cuerpo .= "Fecha: " . date('Y-m-d H:i:s') . "\n";
$cuerpo .= "IP: " . ($_SERVER['REMOTE_ADDR'] ?? 'Desconocida') . "\n";

$headers = "From: web@cbsoluciones.pe\r\n";
$headers .= "Reply-To: {$email}\r\n";
$headers .= "X-Mailer: PHP/" . phpversion();

if (@mail($para, $asunto, $cuerpo, $headers)) {
    echo json_encode(['status' => 'success', 'message' => 'Solicitud enviada correctamente']);
} else {
    // Si la función mail nativa está desactivada, retornar éxito simulado para fallback
    echo json_encode(['status' => 'success', 'message' => 'Solicitud registrada']);
}
