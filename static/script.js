document.getElementById('resenaForm').addEventListener('submit', async (e) => {
    e.preventDefault(); // Evita que la página se refresque

    const input = document.getElementById('resenaInput');
    const container = document.getElementById('resultado-container');
    const btn = document.getElementById('submitBtn');
    
    const texto = input.value.trim();
    if (!texto) return;

    // Estado de carga
    btn.disabled = true;
    btn.innerText = "La IA está pensando...";
    container.innerHTML = ""; 

    try {
        // Petición al endpoint de Flask
        const response = await fetch('/analizar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ resena: texto })
        });

        if (!response.ok) throw new Error('Error en el servidor');

        const data = await response.json();

        // Renderizar el resultado bonico
        container.innerHTML = `
            <div class="resultado ${data.clase}">
                <p>${data.mensaje}</p>
            </div>
        `;

        // Limpiar el textarea si fue positivo
        if(data.clase === 'positivo') input.value = "";

    } catch (error) {
        container.innerHTML = `
            <div class="resultado negativo">
                <p>Oye, algo ha fallado en la conexión. Inténtalo de nuevo.</p>
            </div>
        `;
        console.error("Error:", error);
    } finally {
        btn.disabled = false;
        btn.innerText = "Enviar mi opinión";
    }
});