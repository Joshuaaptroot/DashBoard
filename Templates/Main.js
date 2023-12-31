        // Fetch and render execution time chart
        console.log('Fetching data...');
        fetch('/api/RobotMetrics')
            .then(response => response.json())
            .then(data => {
                console.log('Data received:', data);
                // Rest of your code
            });

        fetch('/api/RobotMetrics')
            .then(response => response.json())
            .then(data => {
                const executionTimes = data.map(item => item.Execution_Time);
                const assignees = data.map(item => item.Assignee);

                const ctxExecutionTime = document.getElementById('executionTimeChart').getContext('2d');
                new Chart(ctxExecutionTime, {
                    type: 'bar',
                    data: {
                        labels: assignees,
                        datasets: [{
                            label: 'Execution Time',
                            data: executionTimes,
                            backgroundColor: 'rgba(255, 99, 132, 0.2)',
                            borderColor: 'rgba(255, 99, 132, 1)',
                            borderWidth: 1
                        }]
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: {
                                beginAtZero: true
                            },
                            x: {
                                display: false
                            }
                        }
                    }
                });
            });