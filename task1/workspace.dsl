workspace {
    name "File Storage System"
    description "Architecture for a file storage system similar to Google Drive"

    model {
        user = person "User" "System user who uploads and manages files" {
            tags "Customer"
        }

        auth_service = softwareSystem "Auth Service" "Handles authentication and authorization" {
            tags "ExternalSystem"
        }

        file_storage_system = softwareSystem "File Storage System" "Handles file storage and user management" {
            group "Core Services" {
                user_api = container "User API" "Manages user accounts and authentication requests" "GoLang" "Container"
                storage_service = container "Storage Service" "Handles file and folder operations" "GoLang" "Container"
                database = container "Database" "Stores users, files, and folder metadata" "PostgreSQL" "Database"
                object_storage = container "Object Storage" "Stores actual file contents" "S3-compatible Storage" "ExternalSystem"
            }
        }

        user -> user_api "Creates an account, manages files and folders"
        user_api -> auth_service "Authenticates user" "REST API"
        user_api -> database "Stores user and metadata" "SQL"
        user_api -> storage_service "Requests file operations" "REST API"
        storage_service -> database "Manages file metadata" "SQL"
        storage_service -> object_storage "Stores and retrieves file contents" "REST API"
    }

    views {
        systemContext file_storage_system "Context" {
            include *
            autoLayout
        }

        container file_storage_system "Containers" {
            include *
            autoLayout
        }

        component storage_service "Storage-Service-Components" {
            include *
            autoLayout
        }

        styles {
            element "Person" {
                color #ffffff
                fontSize 22
                shape Person
            }
            element "Container" {
                background #438dd5
                color #ffffff
            }
            element "Database" {
                shape Cylinder
            }
            element "ExternalSystem" {
                background #c0c0c0
                color #ffffff
            }
        }
    }
}
