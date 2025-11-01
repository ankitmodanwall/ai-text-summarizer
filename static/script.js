document.addEventListener('DOMContentLoaded', function() {
    const inputText = document.getElementById('inputText');
    const summarizeBtn = document.getElementById('summarizeBtn');
    const clearBtn = document.getElementById('clearBtn');
    const copyBtn = document.getElementById('copyBtn');
    const outputSection = document.getElementById('outputSection');
    const errorSection = document.getElementById('errorSection');
    const loadingSection = document.getElementById('loadingSection');
    const summaryText = document.getElementById('summaryText');
    const errorText = document.getElementById('errorText');
    const originalLength = document.getElementById('originalLength');
    const summaryLength = document.getElementById('summaryLength');
    const reductionPercent = document.getElementById('reductionPercent');

    // Summarize button click handler
    summarizeBtn.addEventListener('click', async function() {
        const text = inputText.value.trim();
        
        if (!text) {
            showError('Please enter some text to summarize');
            return;
        }

        const detailLevel = document.querySelector('input[name="detail"]:checked').value;
        
        // Hide previous results
        outputSection.style.display = 'none';
        errorSection.style.display = 'none';
        loadingSection.style.display = 'block';
        
        try {
            const response = await fetch('/summarize', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    text: text,
                    detail_level: detailLevel
                })
            });

            const data = await response.json();
            
            loadingSection.style.display = 'none';
            
            if (data.success) {
                summaryText.textContent = data.summary;
                originalLength.textContent = data.original_length;
                summaryLength.textContent = data.summary_length;
                
                const reduction = Math.round((1 - data.summary_length / data.original_length) * 100);
                reductionPercent.textContent = reduction + '%';
                
                outputSection.style.display = 'block';
            } else {
                showError(data.error || 'An error occurred during summarization');
            }
        } catch (error) {
            loadingSection.style.display = 'none';
            showError('Failed to connect to the server. Please try again.');
            console.error('Error:', error);
        }
    });

    // Clear button click handler
    clearBtn.addEventListener('click', function() {
        inputText.value = '';
        outputSection.style.display = 'none';
        errorSection.style.display = 'none';
        inputText.focus();
    });

    // Copy button click handler
    copyBtn.addEventListener('click', function() {
        const summary = summaryText.textContent;
        navigator.clipboard.writeText(summary).then(function() {
            const originalText = copyBtn.textContent;
            copyBtn.textContent = '✅ Copied!';
            setTimeout(function() {
                copyBtn.textContent = originalText;
            }, 2000);
        }).catch(function(err) {
            console.error('Failed to copy text:', err);
        });
    });

    // Helper function to show errors
    function showError(message) {
        errorText.textContent = message;
        errorSection.style.display = 'block';
        setTimeout(function() {
            errorSection.style.display = 'none';
        }, 5000);
    }

    // Allow Enter key with Ctrl/Cmd to submit
    inputText.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            summarizeBtn.click();
        }
    });
});
