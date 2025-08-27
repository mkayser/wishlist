# base OS + Node runtime
FROM node:20-alpine

# set working dir
WORKDIR /app

# add manifest files first (for build cache)
COPY package*.json ./

# install deps (repeatable, from lockfile)
RUN npm ci

# add the rest of the source
COPY . .

# docs: container listens on 5173
EXPOSE 5173

# start Vite
CMD ["npm","run","dev","--","--host","0.0.0.0","--port","5173"]
