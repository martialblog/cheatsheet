# Printers

OK, so you want to add a new output format. Very good! Here's how you do it. 

Add the new command-line option to the printer group.

```python
help_MyNewPrinter = "The most awesome printer to exist in the observable universe"
printertype.add_argument('-x', help=help_MyNewPrinter, action='store_const', dest='printer', const='MyNewPrinter')
```

Create a new Printer subclass based on the name you just added. It should the implement the printsheet method.

```python
class MyNewPrinter(Printer):
    [...]
```


Add the new Printer type to the PrinterFactory, so the new Printer object can be instantiated.

```python
printer_classes = {
    [...]
    "MyNewPrinter": MyNewPrinter,
    }
```

Extend the unittest to include the new Printer type

```python
def test_PrinterFactory_MyNewPrinter(self):
    self.assertIs(
    cp.PrinterFactory.create_printer("MyNewPrinterPrinter"),
    cp.MyNewPrinter
    )
```
