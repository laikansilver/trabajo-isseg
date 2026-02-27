const express = require('express');
const path = require('path');
const os = require('os');

const app = express();
const PORT = process.env.PORT || 3000;

// Servir archivos estáticos desde la raíz del proyecto (un nivel arriba)
app.use(express.static(path.join(__dirname, '..')));

// Redirigir la ruta raíz al archivo principal
app.get('/', (req, res) => {
    // Redirigir al archivo específico URL-encoded
    // El navegador pedirá /conbinacion%20de%20proyecto/... y express servirá el archivo estático correspondiente
    res.redirect('/conbinacion%20de%20proyecto/ISSEG-Sistema-Solicitudes-Mejorado.html');
});

// Función para obtener la dirección IP local
function getLocalIp() {
    const interfaces = os.networkInterfaces();
    for (const name of Object.keys(interfaces)) {
        for (const iface of interfaces[name]) {
            // Saltamos direcciones internas y no IPv4
            if ('IPv4' !== iface.family || iface.internal) {
                continue;
            }
            return iface.address;
        }
    }
    return 'localhost';
}

app.listen(PORT, '0.0.0.0', () => {
    const ip = getLocalIp();
    console.log(`\nServidor corriendo en:`);
    console.log(`- Local:   http://localhost:${PORT}`);
    console.log(`- Red:     http://${ip}:${PORT}`);
    console.log(`\nPara acceder desde otra máquina en la misma red, usa la dirección de Red.`);
});
