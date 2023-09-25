# aclean

A-Clean is a Django project for the manaegement of a cleaning business.

### Main project features

- deployed and hosted online as a web app
- user log in access (only 1 user level for this system)
- Home page > create new client or search existing clients. Also list of favorite clients
- Each client may have multiple jobs
- Secondary data management for cleaning team, cleaning supplies, equipment listing
- Each job begins with a walkthrough (aka site visit) of the site. This entails media (video or image capture) and notes
- Each job can be broken into tasks, with team members assigned to those tasks
- The system should be able to generate an estimate, agreement form, invoice and task list as pdfs
- once a job is complete, the owner can review the job and team performance, make notes, etc
- Long term tracking of revenue and expenses on dashboard

### Technical features

- All views are presented in form fields that can be edited and saved without going to a separate page
- The navigation will be "stuck" to the bottom of the page (menu, save, back)
- if any changes in a view, clicking "back" will trigger a confirmation before they discard their changes

### Data entities

**clients**
- client_id (int), name (text), address (text), mobile (text), phone2 (text), email (text), whatspp (boolean)

**workers**
- worker_id (int), name (text), phone (text), email (text), whatsapp (boolean)

**jobs**
- job_id (int), client_id (int), create_date (date), description (blob), estimated_job_time (text), start (date), end (date), completed (boolean)

**tasks**
- task_id (int), job_id (int), task_description (text), area (text), assigned_to (int)
- note: assigned_to references worker_id

**job_teams**
- job_id (int), worker_id (int), wage (float)

**supplies** (?)
- supply_id (int), name (text), cost (float), quantity (int), acquired_date (date)

**expenses**
- expense_id (int), job_id (int), item (text), cost (float) 

**site_visits**
- visit_id (int), job_id (int), visit_date (date), vivsit_notes (blob)

**visit_media**
- media_id (int), visit_id (int), filename (text), caption (text)

**job_line_items** (for estimates and invoices)
- line_id (int), job_id (int), description (text), cost (float), on_invoice (boolean)

**job_notes**
- note_id (int), job_id (int), subject (text), note (blob)