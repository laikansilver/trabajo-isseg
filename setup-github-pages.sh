#!/bin/bash

# Script para configurar GitHub Pages y Docker

echo "🚀 Iniciando configuración de GitHub Pages + Docker..."

# Verificar si Git está disponible
if ! command -v git &> /dev/null; then
    echo "❌ Git no está instalado. Por favor instala Git primero."
    exit 1
fi

# Agregar archivos a Git
echo "📝 Agregando archivos de configuración..."
git add CNAME .github/workflows/deploy.yml Dockerfile docker-compose.yml

# Crear commit
echo "💾 Creando commit..."
git commit -m "🚀 Configurar GitHub Pages con subdominio sgspcsi.isseg.com y Docker"

# Hacer push
echo "🌐 Enviando a GitHub..."
git push origin main

echo "✅ Configuración completada!"
echo ""
echo "📋 Próximos pasos:"
echo "1. Ir a: https://github.com/laikansilver/trabajo-isseg/settings/pages"
echo "2. Crear registro TXT en tu DNS:"
echo "   Nombre: _github-pages-challenge-laikansilver.sgspcsi.isseg.com"
echo "   Valor: 60ce5201bb00ef7c746d78c2f81b2e"
echo "3. Esperar 15-30 minutos de propagación"
echo "4. GitHub Pages se autodesplegará automáticamente"
echo ""
echo "🐳 Para ejecutar localmente con Docker:"
echo "   docker-compose up -d"
echo ""
echo "🌍 Accesible en: https://sgspcsi.isseg.com (después de 24h)"
