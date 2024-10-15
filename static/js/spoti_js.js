// Función que se ejecuta cuando el SDK de Spotify está listo
window.onSpotifyWebPlaybackSDKReady = () => {
    // Recuperar el token almacenado
    const token = localStorage.getItem('access_token') || ''; // Asegúrate de que 'access_token' coincida con la clave utilizada para almacenarlo

    // Inicializar el reproductor
    const player = new Spotify.Player({
        name: 'Web Playback SDK Quick Start Player',
        getOAuthToken: cb => { cb(token); }, // Proporcionar el token cuando se necesite
        volume: 0.5
    });

    // Conectar el reproductor
    player.connect().then(success => {
        if (success) {
            console.log('Conectado al reproductor de Spotify');
        }
    }).catch(error => {
        console.error('Error al conectar con el reproductor:', error);
    });
};

// Función para manejar el callback de Spotify
async function callback() {
    try {
        const response = await fetch('http://127.0.0.1:8000/home/auth/callback/', {
            method: 'GET',
            credentials: 'include',
        });

        console.log("Response Status:", response.status);
        console.log("Response Headers:", response.headers);

        // Obtener el texto de la respuesta
        const text = await response.text();
        console.log("Response Text:", text); // Imprimir el texto de la respuesta

        // Verifica si la respuesta es correcta
        if (!response.ok) {
            throw new Error('Failed to fetch access token');
        }

        // Analiza el texto de la respuesta como JSON
        const data = JSON.parse(text);
        console.log("El token se ha generado con éxito:", data.access_token);
        
        // Almacena el token en localStorage
        localStorage.setItem('access_token', data.access_token);
        
        return data.access_token; // Asegúrate de que este sea el campo correcto en tu respuesta
    } catch (error) {
        console.error("Error en callback:", error);
        throw error; // Relanzar el error para que pueda ser capturado más arriba
    }
}
