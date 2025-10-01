# 🌐 Path Parameters and Query Parameters in FastAPI

In FastAPI, **parameters** allow you to pass information from the client to the server. Two of the most common types of parameters are **path parameters** and **query parameters**. Understanding them is crucial for designing flexible and interactive APIs.

---

## 🔹 Path Parameters

### 1️⃣ What are Path Parameters?
- Path parameters are **dynamic segments of the URL path**.  
- They allow the client to specify **which resource** they want to interact with.  
- They are defined in the path itself and are **mandatory** unless a default is provided.

**Example Conceptually:**
- URL: `/users/123` → `123` is a path parameter representing the user ID.  
- Purpose: Identify **a specific resource** in a collection.

### 2️⃣ Characteristics
- **Mandatory**: Usually required to identify the resource.  
- **Typed**: Can enforce data types like `int`, `str`, or `float` for validation.  
- **Used in Routing**: FastAPI uses path parameters to **match URLs to endpoint functions**.

### 3️⃣ Key Points
- Path parameters are **part of the URL**.  
- They are ideal for **resources that are uniquely identified**.  
- Usually corresponds to **RESTful endpoint design**: `/users/{user_id}`, `/products/{product_id}`.

---

## 🔹 Query Parameters

### 1️⃣ What are Query Parameters?
- Query parameters are **optional parameters** appended to the URL after a question mark (`?`).  
- They provide additional **filtering, searching, or sorting** options.

**Example Conceptually:**
- URL: `/users?role=admin&active=true` → `role` and `active` are query parameters.  
- Purpose: Modify or filter the **response data** without changing the resource path.

### 2️⃣ Characteristics
- **Optional**: Can have default values if not provided by the client.  
- **Typed and Validated**: FastAPI can enforce type checks automatically.  
- **Used for Filtering**: Commonly used for pagination, searching, sorting, or specifying options.

### 3️⃣ Key Points
- Query parameters **do not change the resource identity**; they alter the behavior of the response.  
- Can have **multiple parameters** in the same request.  
- Follows the standard **key=value** format separated by `&`.

---

## 🔹 Path Parameters vs Query Parameters
| Feature | Path Parameters | Query Parameters |
|---------|----------------|-----------------|
| Location | Part of the URL path | After `?` in the URL |
| Mandatory | Usually required | Usually optional |
| Purpose | Identify a specific resource | Filter, sort, or modify response |
| Example URL | `/users/123` | `/users?role=admin&active=true` |

### 🔹 Summary
- **Path Parameters**: For identifying a specific resource, part of the URL, typically required.  
- **Query Parameters**: For filtering or modifying responses, appended after `?`, typically optional.  
- FastAPI automatically **validates types**, **parses inputs**, and makes it easy to build **dynamic and flexible APIs** using both.

---

This concept is foundational before moving to **request bodies, form data, and more complex FastAPI features**.

