FROM nginx:alpine
COPY index.html/usr/share/nginx/html/index.html
<!DOCTYPE html>
<html>
<head>
    <title>Hello Docker</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This webpage is running inside a Docker container.</p>
</body>
</html>