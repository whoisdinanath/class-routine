# Class Routine API

This API allows you to retrieve class routines for a specific class.

## Endpoints

### GET /routine

Retrieves the class routine for a specific class.

#### Query Parameters

- `class`: Required. The name of the class for which to retrieve the routine.
- `date`: Optional. The date for which to retrieve the routine. If not provided, the current date will be used.

#### Response

If successful, the response will contain the following data:

- `routine`: An array of objects representing the class routine for the specified class and date. Each object will have the following properties:
  - `startTime`: The start time of the class.
  - `endTime`: The end time of the class.
  - `subject`: The subject of the class.
  - `teacher`: The name of the teacher teaching the class.

#### Example

