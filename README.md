# SQLAlchemy Parameter Filler

A flask extension to replace SQLA parameter markers with string values.

```
SELECT * FROM customers WHERE customer_id = :customer_id AND customer_name LIKE '%:customer_name%'
```

...surfaces two parameter markers:

+ **customer_id**
+ **customer_name**

## Why

When testing queries it's hard to find-and-replace all the parameters on every execution. I built this tool to make it easier for a query to go from source control into SSMS.

## Usage

Register this blueprint against your Flask application and visit the root URL.

```
from .fmt_blueprint import bp as fmt_blueprint
app.register_blueprint(fmt_blueprint, url_prefix='/fmt_blueprint')
```

Paste a query including parameter markers into the textbox, click "Find Parameter Markers". Then add values for these parameters and click "Generate SQL". Optionally, you can choose to wrap the replaced values in single quotes.
