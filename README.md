# google_translator_new_po_file

In google_trans_new package there is bug in google_translator method . Need to change 151 line 

```

 response = (decoded_line + ']')

To 

response = decoded_line
```

