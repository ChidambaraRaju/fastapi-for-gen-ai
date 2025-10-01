# 🌐 HTTP Status Codes

When building APIs or web applications, understanding **HTTP status codes** is crucial. They allow the **server to communicate the result of a client’s request** clearly and systematically.

---

## 🔹 What are HTTP Status Codes?
HTTP status codes are **three-digit numbers** returned by a server in response to a client’s request. They indicate whether the request was successful, resulted in an error, or requires further action.

- Status codes are part of the **HTTP response**.  
- They **help clients understand the outcome** without inspecting the full response body.  
- They are standardized so all clients and servers interpret them consistently.

---

## 🔹 Categories of Status Codes
HTTP status codes are grouped into **five classes**, based on the first digit of the code.

### 1️⃣ 1xx: Informational
- **Range**: 100–199
- **Purpose**: Inform the client that the request was received and is being processed.  
- **Characteristics**: Rarely used in everyday web applications. Mostly handled internally by browsers or intermediaries.
- **Example scenario**: The server acknowledges that the request headers were received and is continuing to process.

### 2️⃣ 2xx: Success
- **Range**: 200–299
- **Purpose**: Indicates that the request was successfully received, understood, and accepted.
- **Common Codes**:
  - **200 OK**: The request was successful, and the server returned the requested data.  
  - **201 Created**: A new resource was successfully created (common in APIs for POST requests).  
  - **204 No Content**: The request was successful but there is no content to return (common for DELETE requests).
- **Key Point**: 2xx codes indicate that everything went as expected.

### 3️⃣ 3xx: Redirection
- **Range**: 300–399
- **Purpose**: Informs the client that further action is needed to complete the request.  
- **Common Codes**:
  - **301 Moved Permanently**: The resource has been moved permanently to a new URL.  
  - **302 Found**: The resource is temporarily available at a different URL.  
  - **304 Not Modified**: The client can use the cached version of the resource; no need to download again.
- **Key Point**: Redirection codes guide clients to the correct location or resource version.

### 4️⃣ 4xx: Client Errors
- **Range**: 400–499
- **Purpose**: Indicates that the request contains an error or cannot be fulfilled by the server.  
- **Common Codes**:
  - **400 Bad Request**: The request is malformed or contains invalid syntax.  
  - **401 Unauthorized**: Authentication is required or failed.  
  - **403 Forbidden**: The client does not have permission to access the resource.  
  - **404 Not Found**: The requested resource does not exist on the server.  
  - **409 Conflict**: There is a conflict with the current state of the resource (common in PUT requests).
- **Key Point**: 4xx codes indicate issues **caused by the client**.

### 5️⃣ 5xx: Server Errors
- **Range**: 500–599
- **Purpose**: Indicates that the server encountered an error while processing a valid request.  
- **Common Codes**:
  - **500 Internal Server Error**: A generic error occurred on the server.  
  - **502 Bad Gateway**: The server received an invalid response from an upstream server.  
  - **503 Service Unavailable**: The server is temporarily overloaded or under maintenance.  
  - **504 Gateway Timeout**: The server did not receive a timely response from an upstream server.
- **Key Point**: 5xx codes indicate issues **caused by the server**.

---

## 🔹 Why Status Codes are Important
- **Communication**: Allows clients to understand the outcome of a request without reading the entire response.  
- **Error Handling**: Clients can handle errors gracefully based on status codes.  
- **Automation**: Many tools, browsers, and scripts rely on status codes to determine next steps (e.g., retry, redirect, log error).  
- **RESTful APIs**: Status codes are integral in REST APIs to indicate success, creation, or errors in a standardized way.

---

## 🔹 Summary
- **1xx**: Informational – request is being processed.  
- **2xx**: Success – request was successfully completed.  
- **3xx**: Redirection – further action required to reach the resource.  
- **4xx**: Client Errors – issues caused by the client request.  
- **5xx**: Server Errors – issues caused by the server.

Using the correct status codes ensures **clarity, reliability, and standardization** in web communication and APIs.