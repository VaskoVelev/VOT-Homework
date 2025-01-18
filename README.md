# Проект за Управление на Файлове с MinIO, Keycloak и Flask

## **Описание**
Този проект предоставя REST API за управление на файлове (качване, сваляне, обновяване и изтриване) с помощта на:
- **MinIO**: Локален S3 backend за съхранение на файлове.
- **Keycloak**: Управление на потребителите и автентикация с JWT токени.
- **Flask**: Уеб сървър за REST API.

---

## **Инсталация и Стартиране**

### **1. Изисквания**
- Docker и Docker Compose

### **2. Стартиране на услугите**
1. Клонирайте репозиторията:
   ```bash
   git clone <repository_url>
   cd project_name
   ```

2. Стартирайте Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Уверете се, че услугите са достъпни:
   - MinIO: [http://localhost:9000](http://localhost:9000)
   - Keycloak: [http://localhost:8080](http://localhost:8080)
   - Приложение: [http://localhost:5000](http://localhost:5000)

---

## **Keycloak Конфигурация**

1. Влезте в Keycloak административния панел: [http://localhost:8080](http://localhost:8080).
2. Създайте Realm с име `file-management`.
3. Създайте Client с име `file-management-client` и задайте:
   - **Access Type**: Confidential
   - **Valid Redirect URIs**: `http://localhost:5000/*`
4. Създайте роли и потребители според нуждите.

---

## **Примерни API Заявки**

### **Качване на файл**
```bash
curl -X POST -H "Authorization: Bearer <your_token>" -F "file=@example.txt" http://localhost:5000/upload
```

### **Сваляне на файл**
```bash
curl -X GET -H "Authorization: Bearer <your_token>" http://localhost:5000/download/example.txt
```

### **Обновяване на файл**
```bash
curl -X PUT -H "Authorization: Bearer <your_token>" -F "file=@new_example.txt" http://localhost:5000/update/example.txt
```

### **Изтриване на файл**
```bash
curl -X DELETE -H "Authorization: Bearer <your_token>" http://localhost:5000/delete/example.txt
```