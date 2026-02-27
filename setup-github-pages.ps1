# Script para configurar GitHub Pages y Docker en Windows
# Ejecutar como: powershell -ExecutionPolicy Bypass -File setup-github-pages.ps1

Write-Host "🚀 Iniciando configuración de GitHub Pages + Docker..." -ForegroundColor Green

# Verificar si Git está disponible
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Git no está instalado. Por favor instala Git primero." -ForegroundColor Red
    exit 1
}

# Verificar si estamos en un repositorio Git
if (-not (Test-Path ".git")) {
    Write-Host "❌ No estás en un repositorio Git. Navega al directorio correcto." -ForegroundColor Red
    exit 1
}

# Agregar archivos a Git
Write-Host "📝 Agregando archivos de configuración..." -ForegroundColor Yellow
git add CNAME .github/workflows/deploy.yml Dockerfile docker-compose.yml Dockerfile

# Crear commit
Write-Host "💾 Creando commit..." -ForegroundColor Yellow
git commit -m "🚀 Configurar GitHub Pages con subdominio sgspcsi.isseg.com y Docker"

# Hacer push
Write-Host "🌐 Enviando a GitHub..." -ForegroundColor Yellow
git push origin main

Write-Host "`n✅ Configuración completada!" -ForegroundColor Green
Write-Host "`n📋 Próximos pasos:" -ForegroundColor Cyan
Write-Host "1. Ir a: https://github.com/laikansilver/trabajo-isseg/settings/pages"
Write-Host "2. Verificar que Settings > Pages muestre la rama 'main' y dominio 'sgspcsi.isseg.com'"
Write-Host "`n3. Crear registro TXT en tu proveedor DNS (GoDaddy, Namecheap, etc):"
Write-Host "   Tipo: TXT"
Write-Host "   Nombre: _github-pages-challenge-laikansilver.sgspcsi.isseg.com"
Write-Host "   Valor: 60ce5201bb00ef7c746d78c2f81b2e"
Write-Host "   TTL: 3600 (o dejar por defecto)"
Write-Host "`n4. Esperar 15-30 minutos de propagación DNS (máximo 24h)"
Write-Host "`n5. GitHub Pages se autodesplegará automáticamente"
Write-Host "`n🐳 Para ejecutar localmente con Docker:"
Write-Host "   docker build -t isseg-sistema ."
Write-Host "   docker run -p 3000:3000 isseg-sistema"
Write-Host "`n   O con Docker Compose:"
Write-Host "   docker-compose up -d"
Write-Host "`n🌍 Accesible en: https://sgspcsi.isseg.com (después de 24h max)"
Write-Host "`n⏱️ El proceso completo toma 24 horas máximo" -ForegroundColor Cyan
