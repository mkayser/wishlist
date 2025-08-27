FROM node:20-alpine        # base OS + Node runtime
WORKDIR /app               # set working dir
COPY package*.json ./      # add manifest files first (for build cache)
RUN npm ci                 # install deps (repeatable, from lockfile)
COPY . .                   # add the rest of the source
EXPOSE 5173                # docs: container listens on 5173
CMD ["npm","run","dev","--","--host","0.0.0.0","--port","5173"]  # start Vite
