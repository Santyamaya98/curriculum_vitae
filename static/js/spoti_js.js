window.onSpotifyWebPlaybackSDKReady = () => {
    // Recuperar el token almacenado
    const token = localStorage.getItem('access_token') || ''; // Asegúrate de que 'access_token' coincida con la clave utilizada para almacenarlo

    const player = new Spotify.Player({
        name: 'Web Playback SDK Quick Start Player',
        getOAuthToken: cb => { cb(token); },
        volume: 0.5
    });

    // Iniciar el reproductor (ejemplo)
    player.connect();
};