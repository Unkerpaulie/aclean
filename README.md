# aclean

A-Clean is a Django project for the management of a cleaning business.

### Main project features

- deployed and hosted online as a web app
- user log in access (only 1 user level for this system)
- Home page > create new client or search existing clients. Also list of favorite clients
- Each client may have multiple jobs
- Secondary data management for workes, cleaning supplies, possibly equipment listing
- Each job begins with a walkthrough (aka site visit) of the site. This entails media (video or image capture) and notes
- Each job can be broken into tasks, with team members assigned to those tasks
- The system should be able to generate an estimate, agreement form, invoice and task list as pdfs
- once a job is complete, the owner can review the job and team performance, make notes, etc
- Long term tracking of revenue and expenses on dashboard

### Technical features

- All views are presented in form fields that can be edited and saved without going to a separate page
- The navigation will be "stuck" to the bottom of the page (menu, save, back)
- if any changes in a view, clicking "back" will trigger a confirmation before they discard their changes
- subsections of pages would be displayed in "accordian" elements that can be expanded or hidden

### Data entities

**clients**
- client_id (int), name (text), address (text), mobile (text), phone2 (text), email (text), whatspp (boolean)

**workers**
- worker_id (int), name (text), phone (text), email (text), whatsapp (boolean), available (boolean)

**jobs**
- job_id (int), client_id (int), create_date (date), description (blob), estimated_job_time (text), start (date), end (date), completed (boolean)

**tasks**
- task_id (int), job_id (int), task_description (text), area (text), assigned_to (int)
- note: assigned_to references worker_id

**job_teams** (not needed, resolved using many-to-many field)
- job_id (int), worker_id (int), wage (float)

**supplies** (?)
- supply_id (int), name (text), cost (float), quantity (int), acquired_date (date)

**expenses**
- expense_id (int), job_id (int), item (text), cost (float) 

**site_visits**
- visit_id (int), job_id (int), visit_date (date), visit_notes (blob)

**visit_media**
- media_id (int), visit_id (int), filename (text), caption (text)

**charge_line_items** (for estimates and invoices)
- line_id (int), job_id (int), description (text), cost (float), on_invoice (boolean)

**job_notes**
- note_id (int), job_id (int), subject (text), note (blob)

### Routes

`/` 
- main page 
- Enter (to go to clients, which is the main app)
- Settings/admin (?) accordian
  - Workers
  - Supplies
  - reports (to be implemented in the future)

`/clients` 
- Add new client, client search, favorite clients list

`/clients/new` 
- new client form

`/clients/<id>` 
- view/edit client info (form), add job, current job (if any), list past jobs

`/jobs/<id>` 
- view/edit description, job time, start/end dates, completed
- add site visit
- view/edit existing site visit
- set/edit worker team
- create/update task list
- create/update expenses list
- create/update charge items
- generate estimate (based on charge items)
- generate invoice
- add/edit job notes


`/workers`
- add/edit worker info

`/supplies`
- add/edit supplies info

### Apps

**main**

**clients**

**jobs**

**workers**

**supplies**