workspace {
    name "Хранилище файлов"
    !identifiers hierarchical

    model {
        user = person "Пользователь" "Загружает, удаляет, ищет файлы и управляет папками"

        fileStorageSystem = softwareSystem "File Storage System" "Приложение для хранения файлов в папках (аналог Яндекс.Диск)" {

            userService = container "User Service" {
                description "Создание пользователя, поиск по логину, поиск по имени и фамилии"
                technology "Python FastAPI"
            }

            folderService = container "Folder Service" {
                description "Создание папок, получение списка всех папок, удаление папок"
                technology "Python FastAPI"
            }

            fileService = container "File Service" {
                description "Создание (загрузка) нового файла в указанную папку, получение файла по имени, удаление файла"
                technology "Python FastAPI"

                fileApiRouter = component "File API Router" {
                    description "Обрабатывает входящие REST-запросы, связанные с файлами, и перенаправляет их"
                    technology "FastAPI Routing"
                }

                fileUpload = component "File Upload Handler" {
                    description "Обрабатывает логику загрузки нового файла в указанную папку"
                    technology "Python"
                }

                fileRetrieval = component "File Retrieval Handler" {
                    description "Обрабатывает логику поиска и получения файла по имени"
                    technology "Python"
                }

                fileDeletion = component "File Deletion Handler" {
                    description "Обрабатывает удаление файла"
                    technology "Python"
                }

                fileApiRouter -> fileUpload "Приходит запрос на загрузку файла"
                fileApiRouter -> fileRetrieval "Приходит запрос на получение файла"
                fileApiRouter -> fileDeletion "Приходит запрос на удаление файла"
            }

            database = container "Database" {
                description "Хранит информацию о пользователях, папках и файлах"
                technology "PostgreSQL"
            }

            userService -> database "Сохраняет/ищет данные пользователей" "SQL"
            folderService -> database "Сохраняет/ищет информацию о папках" "SQL"
            fileService -> database "Сохраняет/ищет метаданные файлов" "SQL"
        }

        user -> fileStorageSystem "Использует веб/мобильный интерфейс для работы с файлами и папками" "REST/HTTPS"

        user -> fileStorageSystem.userService "Создаёт или ищет пользователя" "REST/HTTPS"
        user -> fileStorageSystem.folderService "Создаёт папку, получает список папок, удаляет папку" "REST/HTTPS"
        user -> fileStorageSystem.fileService "Загружает файл, получает файл по имени, удаляет файл" "REST/HTTPS"

        fileStorageSystem.userService -> user "Результаты поиска/создания пользователя"
        fileStorageSystem.folderService -> user "Результаты создания/удаления папки"
        fileStorageSystem.fileService -> user "Результаты создания/получения/удаления файла"
    }

    views {
        systemContext fileStorageSystem "SystemContext" {
            include *
            autolayout lr
        }

        container fileStorageSystem "ContainerView" {
            include *
            autolayout lr
        }

        component fileStorageSystem.fileService "FileServiceComponents" {
            include *
            autolayout lr
        }

        dynamic fileStorageSystem "CreateFile" "Сценарий: загрузка нового файла в папку" {
            user -> fileStorageSystem.userService "Проверка и аутентификация пользователя (при необходимости)"
            user -> fileStorageSystem.folderService "Уточняет, что папка существует или создаёт папку"
            user -> fileStorageSystem.fileService "Отправляет запрос на загрузку файла"
            fileStorageSystem.fileService -> fileStorageSystem.database "Сохраняет метаданные о файле"
            fileStorageSystem.database -> fileStorageSystem.fileService "Подтверждение: данные о файле сохранены"
            fileStorageSystem.fileService -> user "Возвращает ответ: файл загружен"
        }
    }
}
