document.addEventListener('DOMContentLoaded', () => {
    const analyzeButton = document.getElementById('analyzeButton');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const logOutput = document.getElementById('logOutput').querySelector('code');
    const aiResultsDiv = document.getElementById('aiResults');
    const attackResultDiv = document.getElementById('attackResult');

    analyzeButton.addEventListener('click', async () => {
        // --- UI Reset and Loading State ---
        analyzeButton.disabled = true;
        loadingIndicator.style.display = 'flex';
        logOutput.textContent = '[INFO] Starting analysis...';
        aiResultsDiv.innerHTML = '<p>Waiting for AI analysis...</p>';
        attackResultDiv.innerHTML = ''; // Clear previous attack result

        try {
            // --- Call Backend API ---
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                    // No body needed if we are just triggering based on hardcoded data
                }
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            // --- Update Logs ---
            logOutput.textContent = data.logs.join('\n');

            // --- Display AI Analysis ---
            if (data.results && data.results.ai_analysis_structured) {
                const analysis = data.results.ai_analysis_structured;
                let aiHtml = '<h3>AI Analysis Summary</h3>';

                aiHtml += `<p><strong>Themes/Keywords:</strong> ${analysis.themes_keywords || 'N/A'}</p>`;
                aiHtml += `<p><strong>Potential Usernames:</strong> ${analysis.potential_usernames || 'N/A'}</p>`;
                aiHtml += `<p><strong>Suggested Vector:</strong> ${analysis.suggested_vector || 'N/A'}</p>`;

                if (analysis.targeted_password_ideas && analysis.targeted_password_ideas.length > 0) {
                    aiHtml += '<h3>Targeted Password Ideas</h3><ul>';
                    analysis.targeted_password_ideas.forEach(pw => {
                        aiHtml += `<li>${escapeHtml(pw)}</li>`; // Escape potential HTML in passwords
                    });
                    aiHtml += '</ul>';
                } else {
                     aiHtml += '<p><strong>Targeted Password Ideas:</strong> No specific ideas generated.</p>';
                }
                 aiResultsDiv.innerHTML = aiHtml;
            } else {
                 aiResultsDiv.innerHTML = '<p class="error-message">Failed to retrieve or parse AI analysis.</p>';
            }

            // --- Display Attack Result ---
            if (data.results) {
                 if (data.results.attack_success) {
                    attackResultDiv.innerHTML = `<div class="success-message">Attack Simulation Result: SUCCESS! <br>Password: <strong>${escapeHtml(data.results.cracked_password || 'N/A')}</strong></div>`;
                } else if (data.results.cracked_password === null && data.results.attack_success === false ) {
                     // Only show failure if the attack was actually attempted but failed
                     attackResultDiv.innerHTML = `<div class="error-message">Attack Simulation Result: FAILURE! Password not found.</div>`;
                 } else if (data.status === 'error'){
                    // Error occurred before attack simulation could run
                     attackResultDiv.innerHTML = `<div class="error-message">Attack Simulation Result: Skipped due to earlier errors.</div>`;
                 }
            }

        } catch (error) {
            console.error('Error during analysis:', error);
            logOutput.textContent += `\n[ERROR] Frontend Error: ${error.message}`;
            aiResultsDiv.innerHTML = `<p class="error-message">An error occurred while contacting the backend.</p>`;
        } finally {
            // --- Reset UI ---
            loadingIndicator.style.display = 'none';
            analyzeButton.disabled = false;
        }
    });

    // Helper function to escape HTML special characters
    function escapeHtml(unsafe) {
        if (typeof unsafe !== 'string') return unsafe; // Return non-strings directly
        return unsafe
             .replace(/&/g, "&")
             .replace(/</g, "<")
             .replace(/>/g, ">")
             .replace(/"/g, """)
             .replace(/'/g, "'");
     }
});
