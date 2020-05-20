job "example" {
    datacenters = [
        "dc1"
    ]

    group "example" {
        task "example"{
            driver = "docker"

            config {
                image = "j0rzsh/example-flask-api:0.0.1"
            }

            resources {
                cpu = 500
                memory = 256
            

            network {
                mbits = 10

                port "http" {
                    static = "8000"
                }
            }
            }
        }
    }
}
