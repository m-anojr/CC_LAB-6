pipeline {
    agent any

    stages {
        stage('Build Backend Image') {
            steps {
                // Building the image using the 'backend' folder in your repo root
                sh 'docker build -t backend-app backend' [cite: 303, 547]
            }
        }

        stage('Deploy Backends') {
            steps {
                sh '''
                # Create network if it doesn't exist
                docker network create app-network || true
                
                # Remove existing containers to avoid naming conflicts [cite: 341, 560]
                docker rm -f backend1 backend2 || true
                
                # Run two instances of the backend on the shared network [cite: 346, 561]
                docker run -d --name backend1 --network app-network backend-app
                docker run -d --name backend2 --network app-network backend-app
                
                # Delay to allow backends to start before NGINX reloads [cite: 749]
                sleep 5
                '''
            }
        }

        stage('Deploy NGINX') {
            steps {
                sh '''
                # Remove existing NGINX container [cite: 479, 566]
                docker rm -f nginx-lb || true
                
                # Run NGINX on port 80 and link the configuration file [cite: 482, 568-570]
                # Note: path used is relative to the workspace root
                docker run -d --name nginx-lb --network app-network -p 80:80 \
                -v $(pwd)/nginx/default.conf:/etc/nginx/conf.d/default.conf:ro nginx
                
                # Small delay to ensure NGINX is up before reload [cite: 750]
                sleep 2
                
                # Reload NGINX to apply the config [cite: 727]
                docker exec nginx-lb nginx -s reload
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully, NGINX load balancer is running.' [cite: 461, 488]
        }
        failure {
            echo 'Pipeline failed. Check console logs for errors.' [cite: 738]
        }
    }
}
