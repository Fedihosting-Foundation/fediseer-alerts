# Module fediseer_alerts.models

## Classes

`ActivityReport(source_domain: str, target_domain: str, report_type: fediseer_alerts.models.Report_Type, report_activity: fediseer_alerts.models.Report_Activity, created: str)`
:

```
### Class variables

`created: str`
:

`report_activity: fediseer_alerts.models.Report_Activity`
:

`report_type: fediseer_alerts.models.Report_Type`
:

`source_domain: str`
:

`target_domain: str`
:
```

`Report_Activity(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   An enumeration.

```
### Ancestors (in MRO)

* enum.Enum

### Class variables

`ADDED`
:

`DELETED`
:

`MODIFIED`
:
```

`Report_Type(value, names=None, *, module=None, qualname=None, type=None, start=1)`
:   An enumeration.

```
### Ancestors (in MRO)

* enum.Enum

### Class variables

`ACTIVITY`
:

`CENSURE`
:

`GUARANTEE`
:

`HESITATION`
:
```
