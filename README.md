# evreka-case

## Qestion1 

### Tech Stack
- **Server:** Python, Django and Django-Rest Framework
- **Database:** PostreSql

### API Reference
#### Get api root

```http
  GET /api/
```

#### Get Navigation records in the last 48 hours 
```http
  GET /api/records
```

### Important Points
- @property is used in the navigation record model to get the sample output given in the question correctly
- prefetch_related is used in the orm query to increase performance
- function based views is used instead of class based views because the endpoint number was quite low
- Database had 4 navigation data but only 3 of them revealed because of the 48 hour filter.

![Sample](https://github.com/emrpla/evreka-case/blob/main/images/results.PNG)
