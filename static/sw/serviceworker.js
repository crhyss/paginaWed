const nombreCashe = 'pwa-v1';

self.addEventListener('install', function(event){
    console.log('sw se es   ta instalando')
    event.waitUntil(
        caches.open(nombreCashe)
        .then(function(cacheEncontrada){
            return cacheEncontrada.addAll([
                '/'
            ]);
        })
    );
});