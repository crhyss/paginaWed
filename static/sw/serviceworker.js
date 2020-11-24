const nombreCache = 'pwa-v1';

self.addEventListener('install', function(event) {
    console.log("sw se esta instalando...")
    event.waitUntil(
        caches.open(nombreCache)
            .then(function(cacheEncontrada){
                return cacheEncontrada.addAll([
                    '/',
                    '/lista/1',
                    'lista/2',
                    '/productos/1',
                    '/productos/2'
                ]);
            })
    );
});

self.addEventListener("fetch",function(event){
    console.log("El navegador esta pidiendo la pagina..." + event.request);
    event.respondWith(
        caches.match(event.request)
        .then(function(cacheEncontrada){
            if(cacheEncontrada){
                return cacheEncontrada
            }
            return fetch(event.request)
        })
    )
});