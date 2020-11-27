const nombreCache = 'pwa-v0';
var urls = [
  '/',
  '/lista/1',
  '/productos/1',

];
const OFFLINE_CACHE = 'pwa-offline-v0'
const OFFLINE_URL = ['/offline/'];

self.addEventListener('install', function (event) {
  console.log("sw se esta instalando...")
  event.waitUntil(
    caches.open(nombreCache)
      .then(function (cacheEncontrada) {
        return cacheEncontrada.addAll(urls);
      })
  );
});
self.addEventListener('install', function (event) {
    event.waitUntil(
      caches.open(OFFLINE_CACHE)
        .then(function (cacheEncontrada) {
          return cacheEncontrada.addAll(OFFLINE_URL);
        })
    ); 
});

//   responde a todas las peticiones con el contenido de la red. Si falla intenta responder con el contenido del Cache Storage.
self.addEventListener("fetch", function(event) {
  event.respondWith(
    fetch(event.request).catch(function() {
      return caches.match(event.request).then(function(response) {
        return response || caches.match("/offline/");
      });
    })
  );
});


