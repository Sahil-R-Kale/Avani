document.addEventListener('DOMContentLoaded', function() {
    // Handle form submission for adding farmer data
    document.getElementById('farmerForm').addEventListener('submit', function(event) {
        event.preventDefault();
        
        const formData = new FormData();
        formData.append('farmer_name', event.target.farmer_name.value);
        formData.append('timestamps', event.target.timestamp.value);  
        formData.append('audio', event.target.audio.files[0]);

        fetch('BACKEND_URL/process_audio', { // Replace with your actual API URL
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').textContent = data.message;
        })
        .catch(error => {
            document.getElementById('response').textContent = 'Error: ' + error;
        });
    });

    document.getElementById('viewFarmerDataForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData();
        formData.append('farmer_name', event.target.farmer_name_view.value);

        fetch('BACKEND_URL/show_data', { // Replace with your actual API URL
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            const farmerData = data.data; // 
            const table = document.getElementById('farmerDataTable');

            table.innerHTML = '';
            const desiredOrder = ['Farmer Name', 'Taluka', 'Village', 'Land size used for Onion', 'Last Soil Testing', 'Quantity of seeds sown', 'Water source/s for the farm', 'Availability of water in the last season','Availability of Electricity in the last season','Availability of Labour in the last season','Production estimate for this season','Storage conditions'];

            // Sort the farmerData based on the desired order
            desiredOrder.forEach(key => {
                if (farmerData[key] !== undefined) {
                    const row = table.insertRow();
                    const cell1 = row.insertCell(0);
                    const cell2 = row.insertCell(1);
                    cell1.textContent = key;
                    cell1.style.fontWeight = 'bold'; // Make the first column bold
                    cell2.textContent = farmerData[key];

                    if (farmerData[key].toLowerCase().includes('yes')) {
                        cell2.classList.add('green-text');
                    } else if (farmerData[key].toLowerCase().includes('no')) {
                        cell2.classList.add('red-text');
                    }
                    else if (farmerData[key].toLowerCase().includes('problem')) {
                        cell2.classList.add('red-text');
                    }
                    else if (farmerData[key].toLowerCase().includes('manageable')) {
                        cell2.classList.add('yellow-text');
                    }
                }
            });
        })
        .catch(error => {
            document.getElementById('viewResponse').textContent = 'Error: No data found, please try again!';
        });
    });
        // Handle insights form submission
        function handleInsightsRequest(buttonText) {
            const form = document.getElementById('insightsForm');
            const formData = new FormData(form);
    
            formData.append('button_pressed', buttonText);
    
            fetch('BACKEND_URL/get_insights', { // Replace with your actual API URL
                method: 'POST',
                body: formData,
            })
            .then(response => {
                if (buttonText === 'Graphical Insights') {
                    return response.blob(); // Get the image blob if it's a graphical insight
                } else {
                    return response.json(); // Get JSON data for textual insights
                }
            })
            .then(data => {
                const insightsList = document.getElementById('insightsList');
                insightsList.innerHTML = ''; // Clear previous insights
    
                if (buttonText === 'Graphical Insights') {
                    const imageUrl = URL.createObjectURL(data);
                    const imgElement = document.createElement('img');
                    imgElement.src = imageUrl;
                    imgElement.alt = 'Graphical Insights';
                    imgElement.style.maxWidth = '100%'; 
                    imgElement.style.marginTop = '20px';
                    insightsList.appendChild(imgElement);
                } else {
                    data.data.forEach(insight => {
                        const listItem = document.createElement('li');
                        listItem.textContent = insight;
                        insightsList.appendChild(listItem);
                    });
                }
            })
            .catch(error => {
                document.getElementById('insightsResponse').textContent = 'Error: ' + error;
            });
        }
    
        // Add event listeners for the buttons
        document.getElementById('textualInsights').addEventListener('click', function() {
            handleInsightsRequest('Textual Insights');
        });
    
        document.getElementById('graphicalInsights').addEventListener('click', function() {
            handleInsightsRequest('Graphical Insights');
        });
});
