Use csrf_token when you are sending a form or browser request that changes data in a Django app and the request is protected by Django's session-based CSRF system.

In simple terms, it belongs in forms that use POST, PUT, PATCH, or DELETE behavior, especially when the request comes from a browser page. Django checks this token to make sure the request really came from your site and not from a fake external page.

You usually add it inside a template form like this:

{% csrf_token %}

You should use it for normal Django HTML forms and for JavaScript requests that send cookies or use session authentication. You do not need it for safe GET requests, because GET should only read data and not change anything.

The main mistake is leaving it out of a form that changes data. Then Django will reject the request with a CSRF verification error. Another common mistake is assuming APIs always need it. If you are using token-based authentication or a pure API setup, CSRF may not be the right tool in the same way.

Big picture: csrf_token is Django's way of protecting users from forged requests. Use it whenever a browser-based request changes server data and Django expects CSRF protection.