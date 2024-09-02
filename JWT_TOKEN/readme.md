# JWT Authentication API Documentation

### Overview

This documentation describes the JWT authentication setup and how to perform `POST`, `DELETE`, and `UPDATE` operations on your API using JWT authentication.

### 1. Obtain JWT Token

**Endpoint**: `/gettoken/`  
**Method**: `POST`  
**Description**: Obtain access and refresh tokens using user credentials.

#### Request

**URL**: `http://localhost:8000/gettoken/`  
**Headers**: `Content-Type: application/x-www-form-urlencoded`  
**Body** (x-www-form-urlencoded):

- `username`: Your username
- `password`: Your password

#### Response

**Success (200 OK)**:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

**Error (400 Bad Request)**:

```json
{
  "non_field_errors": ["Unable to log in with provided credentials."]
}
```

### 2. Refresh JWT Token

**Endpoint**: `/tokenrefresh/`  
**Method**: `POST`  
**Description**: Refresh the access token using a valid refresh token.

#### Request

**URL**: `http://localhost:8000/tokenrefresh/`  
**Headers**: `Content-Type: application/x-www-form-urlencoded`  
**Body** (x-www-form-urlencoded):

- `refresh`: Your refresh token

#### Response

**Success (200 OK)**:

```json
{
  "access": "new_access_token"
}
```

**Error (400 Bad Request)**:

```json
{
  "refresh": ["The given token is expired."]
}
```

### 3. Verify JWT Token

**Endpoint**: `/verifytoken/`  
**Method**: `POST`  
**Description**: Verify the validity of the provided access token.

#### Request

**URL**: `http://localhost:8000/verifytoken/`  
**Headers**: `Content-Type: application/x-www-form-urlencoded`  
**Body** (x-www-form-urlencoded):

- `token`: Your access token

#### Response

**Success (200 OK)**:

```json
{
  "status": "valid"
}
```

**Error (400 Bad Request)**:

```json
{
  "token": ["Token is invalid or expired."]
}
```

### 4. Create Resource (POST)

**Endpoint**: `/api/resource/`  
**Method**: `POST`  
**Description**: Create a new resource. Requires a valid access token for authorization.

#### Request

**URL**: `http://localhost:8000/api/resource/`  
**Headers**:

- `Authorization: Bearer your_access_token`
- `Content-Type: application/json`

**Body** (JSON):

```json
{
  "field1": "value1",
  "field2": "value2"
}
```

#### Response

**Success (201 Created)**:

```json
{
  "id": "resource_id",
  "field1": "value1",
  "field2": "value2"
}
```

**Error (400 Bad Request)**:

```json
{
  "field1": ["This field is required."]
}
```

### 5. Update Resource (PUT/PATCH)

**Endpoint**: `/api/resource/{id}/`  
**Method**: `PUT` or `PATCH`  
**Description**: Update an existing resource. Requires a valid access token for authorization.

#### Request

**URL**: `http://localhost:8000/api/resource/{id}/`  
**Headers**:

- `Authorization: Bearer your_access_token`
- `Content-Type: application/json`

**Body** (JSON):

```json
{
  "field1": "new_value1",
  "field2": "new_value2"
}
```

#### Response

**Success (200 OK)**:

```json
{
  "id": "resource_id",
  "field1": "new_value1",
  "field2": "new_value2"
}
```

**Error (400 Bad Request)**:

```json
{
  "field1": ["This field is required."]
}
```

### 6. Delete Resource (DELETE)

**Endpoint**: `/api/resource/{id}/`  
**Method**: `DELETE`  
**Description**: Delete an existing resource. Requires a valid access token for authorization.

#### Request

**URL**: `http://localhost:8000/api/resource/{id}/`  
**Headers**:

- `Authorization: Bearer your_access_token`

#### Response

**Success (204 No Content)**:

```json
{
  "detail": "Resource deleted successfully."
}
```

**Error (404 Not Found)**:

```json
{
  "detail": "Not found."
}
```

---

This documentation should help users understand how to interact with your API using JWT authentication for creating, updating, and deleting resources.
