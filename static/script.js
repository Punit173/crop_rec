document.getElementById('cropForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Get form data
    const formData = {
        N: document.getElementById('N').value,
        P: document.getElementById('P').value,
        K: document.getElementById('K').value,
        temperature: document.getElementById('temperature').value,
        humidity: document.getElementById('humidity').value,
        ph: document.getElementById('ph').value,
        rainfall: document.getElementById('rainfall').value
    };

    try {
        // Show loading state
        const predictionElement = document.getElementById('prediction');
        predictionElement.textContent = 'Analyzing...';
        
        // Make API call
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        const data = await response.json();
        
        if (response.ok) {
            // Display prediction
            predictionElement.textContent = data.prediction.charAt(0).toUpperCase() + data.prediction.slice(1);
        } else {
            // Display error
            predictionElement.textContent = 'Error: ' + data.error;
        }
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('prediction').textContent = 'Error: Could not get prediction';
    }
}); 