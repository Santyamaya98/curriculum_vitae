async function callback() {
    try {
        const response = await fetch('spotify_callback', {
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
        return data.access_token; // Asegúrate de que este sea el campo correcto en tu respuesta
    } catch (error) {
        console.error("Error en callback:", error);
        throw error; // Relanzar el error para que pueda ser capturado más arriba
    }
}

window.onSpotifyWebPlaybackSDKReady = async () => {
    try {
        const token = await callback(); // Llamar a la función callback
        console.log("Access Token:", token);

        const player = new Spotify.Player({
            name: 'Web Playback SDK Quick Start Player',
            getOAuthToken: cb => { 
                cb(token); 
                console.log("OAuth token provided:", token); 
            },
            volume: 0.5
        });

        player.addListener('ready', ({ device_id }) => {
            console.log('Ready with Device ID:', device_id);
        });

        player.addListener('not_ready', ({ device_id }) => {
            console.log('Device ID has gone offline:', device_id);
        });

        player.addListener('initialization_error', ({ message }) => {
            console.error('Initialization Error:', message);
        });

        player.addListener('authentication_error', ({ message }) => {
            console.error('Authentication Error:', message);
        });

        player.addListener('account_error', ({ message }) => {
            console.error('Account Error:', message);
        });

        player.addListener('player_state_changed', state => {
            console.log('Player State Changed:', state);
            document.getElementById('trackName').innerText = state.track_window.current_track.name;
        });

        // Botón de Play/Pause
        document.getElementById('togglePlay').onclick = function() {
            console.log("Toggle Play / Pause button clicked");
            player.togglePlay().then(() => {
                console.log("Toggle Play successful");
            }).catch(error => {
                console.error('Play Error:', error);
            });
        };

        // Botón de siguiente pista
        document.getElementById('nextTrack').onclick = function() {
            console.log("Next Track button clicked");
            player.nextTrack().then(() => {
                console.log("Skipped to next track");
            }).catch(error => {
                console.error('Next Track Error:', error);
            });
        };

        // Botón de pista anterior
        document.getElementById('prevTrack').onclick = function() {
            console.log("Previous Track button clicked");
            player.previousTrack().then(() => {
                console.log("Skipped to previous track");
            }).catch(error => {
                console.error('Previous Track Error:', error);
            });
        };

        // Conectar el reproductor
        player.connect().then(success => {
            if (success) {
                console.log('Connected to Spotify Player');
            } else {
                console.error('Failed to connect to Spotify Player');
            }
        }).catch(error => {
            console.error('Connection Error:', error);
        });

    } catch (error) {
        console.error("Error en onSpotifyWebPlaybackSDKReady:", error);
    }
}
