FROM node:18-alpine

WORKDIR /app

# Copiar package files desde la carpeta server (nivel superior)
COPY ../server/package*.json ./

# Instalar dependencias
RUN npm install

# Copiar toda la aplicación desde la raíz
COPY .. .

EXPOSE 3000

ENV NODE_ENV=production

# Ejecutar server desde la carpeta server
WORKDIR /app/server
CMD ["npm", "start"]
