# Class Routine API

This API allows you to retrieve class routines for a specific class.

## Endpoints

### GET api/routine/class
### GET api/routine/teacher

Retrieves the class routine for a specific class.

#### Query Parameters

- `level`: Required. Level for which the routine is to be retrieved.
- `day`: Required. Day for which the routine is required
- `semester` : Required. Semester whose routine is required

#### Response

If successful, the response will contain the following data:

- `routine`: An array of objects representing the class routine for the specified level and day. Each object will have the following properties:
  - `subject`: The subject of the class.
  - `group`: The group for which the class is for.
  - `startTime`: The start time of the class.
  - `endTime`: The end time of the class.
  - `subject`: The subject of the class.
  - `teacher`: The name of the teacher teaching the class.

*** Visit /api endpoint for more details. ***