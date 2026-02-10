Purpose and Scope 
-----------------------------

This document provides a comprehensive overview of the **proyecto-cine** system, a Django-based cinema ticket booking platform. It introduces the system's architecture, core components, and technology stack. For detailed information about specific applications, see [Movies Application](#4), [MovieTheaters Application](#5), and [Users and Tickets Applications](#6). For deployment and configuration details, see [System Architecture](#3).

**Sources:** [README.md1](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/README.md#L1-L1)

* * *

System Purpose 
--------------------------

**proyecto-cine** is a web-based cinema management system that enables users to browse movies, view theater information, and purchase tickets for specific screenings at designated seats. The system manages the complete lifecycle of cinema operations including:

*   Movie catalog management with genre classification
*   Theater and seating capacity management
*   Screening schedule management
*   Ticket booking and user purchase tracking

The system exposes REST API endpoints for programmatic access and provides a Django admin interface for administrative operations.

**Sources:** [backend/docs/diagrams/diagramas-cine.drawio1-514](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/docs/diagrams/diagramas-cine.drawio#L1-L514) [backend/main/settings.py33-45](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L33-L45)

* * *

Technology Stack 
----------------------------

Component

Technology

Configuration Reference

**Web Framework**

Django 5.2.8

[backend/main/settings.py1-128](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L1-L128)

**Database**

SQLite

[backend/main/settings.py80-85](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L80-L85)

**ORM**

Django ORM

Built into Django

**API Layer**

Django Views + Serializers

Application-specific

**Admin Interface**

Django Admin

`django.contrib.admin`

**Application Server**

WSGI/ASGI

[backend/main/wsgi.py](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/wsgi.py) [backend/main/asgi.py](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/asgi.py)

**Sources:** [backend/main/settings.py1-128](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L1-L128)

* * *

Django Project Structure 
------------------------------------

The system follows Django's standard project organization with a main configuration package and four domain-specific applications:

<table><thead><tr><th>Component</th><th>Technology</th><th>Configuration Reference</th></tr></thead><tbody><tr><td><strong>Web Framework</strong></td><td>Django 5.2.8</td><td><a href="https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L1-L128" target="_blank" rel="noopener noreferrer" class="mb-1 mr-1 inline-flex items-stretch font-mono text-xs !no-underline transition-opacity hover:opacity-75"><span class="flex items-center break-all rounded-l px-2 py-1.5 bg-[#e5e5e5] text-[#333333] dark:bg-[#252525] dark:text-[#e4e4e4]"><svg class="mr-1.5 hidden h-3.5 w-3.5 flex-shrink-0 opacity-40 md:block" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"></path></svg>backend/main/settings.py</span><span class="flex flex-shrink-0 items-center rounded-r border-l px-2 py-1.5 border-[#dddddd] bg-[#d8d8d8] text-[#666666] dark:border-[#333333] dark:bg-[#2a2a2a] dark:text-[#888888]">1-128</span></a></td></tr><tr><td><strong>Database</strong></td><td>SQLite</td><td><a href="https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L80-L85" target="_blank" rel="noopener noreferrer" class="mb-1 mr-1 inline-flex items-stretch font-mono text-xs !no-underline transition-opacity hover:opacity-75"><span class="flex items-center break-all rounded-l px-2 py-1.5 bg-[#e5e5e5] text-[#333333] dark:bg-[#252525] dark:text-[#e4e4e4]"><svg class="mr-1.5 hidden h-3.5 w-3.5 flex-shrink-0 opacity-40 md:block" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"></path></svg>backend/main/settings.py</span><span class="flex flex-shrink-0 items-center rounded-r border-l px-2 py-1.5 border-[#dddddd] bg-[#d8d8d8] text-[#666666] dark:border-[#333333] dark:bg-[#2a2a2a] dark:text-[#888888]">80-85</span></a></td></tr><tr><td><strong>ORM</strong></td><td>Django ORM</td><td>Built into Django</td></tr><tr><td><strong>API Layer</strong></td><td>Django Views + Serializers</td><td>Application-specific</td></tr><tr><td><strong>Admin Interface</strong></td><td>Django Admin</td><td><code class="bg-input-dark/30 border-cloud/30 rounded-md border px-[0.25rem] py-px text-xs font-normal leading-[15px] before:hidden after:hidden">django.contrib.admin</code></td></tr><tr><td><strong>Application Server</strong></td><td>WSGI/ASGI</td><td><a href="https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/wsgi.py" target="_blank" rel="noopener noreferrer" class="mb-1 mr-1 inline-flex items-stretch font-mono text-xs !no-underline transition-opacity hover:opacity-75"><span class="flex items-center break-all rounded-l px-2 py-1.5 bg-[#e5e5e5] text-[#333333] dark:bg-[#252525] dark:text-[#e4e4e4] rounded-r"><svg class="mr-1.5 hidden h-3.5 w-3.5 flex-shrink-0 opacity-40 md:block" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"></path></svg>backend/main/wsgi.py</span></a> <a href="https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/asgi.py" target="_blank" rel="noopener noreferrer" class="mb-1 mr-1 inline-flex items-stretch font-mono text-xs !no-underline transition-opacity hover:opacity-75"><span class="flex items-center break-all rounded-l px-2 py-1.5 bg-[#e5e5e5] text-[#333333] dark:bg-[#252525] dark:text-[#e4e4e4] rounded-r"><svg class="mr-1.5 hidden h-3.5 w-3.5 flex-shrink-0 opacity-40 md:block" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"></path></svg>backend/main/asgi.py</span></a></td></tr></tbody></table>

### Application Registry 

The following applications are registered in `INSTALLED_APPS`:

Application

Config Class

Purpose

`movies`

`movies.apps.MoviesConfig`

Movie catalog and genre management

`users`

`users.apps.UsersConfig`

User account management

`tickets`

`tickets.apps.TicketsConfig`

Ticket booking and sales

`movietheaters`

`movietheaters.apps.MovietheatersConfig`

Theater and seat management

**Sources:** [backend/main/settings.py33-45](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L33-L45) [backend/main/settings.py80-85](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L80-L85)

* * *

Domain Model 
------------------------

The system implements a relational data model centered around the ticket booking workflow. The `Ticket` entity serves as the transactional record connecting users, movies, screenings, theaters, and seats.

#mermaid-9locys34zsj{font-family:ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-9locys34zsj .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-9locys34zsj .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-9locys34zsj .error-icon{fill:#a44141;}#mermaid-9locys34zsj .error-text{fill:#ddd;stroke:#ddd;}#mermaid-9locys34zsj .edge-thickness-normal{stroke-width:1px;}#mermaid-9locys34zsj .edge-thickness-thick{stroke-width:3.5px;}#mermaid-9locys34zsj .edge-pattern-solid{stroke-dasharray:0;}#mermaid-9locys34zsj .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-9locys34zsj .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-9locys34zsj .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-9locys34zsj .marker{fill:lightgrey;stroke:lightgrey;}#mermaid-9locys34zsj .marker.cross{stroke:lightgrey;}#mermaid-9locys34zsj svg{font-family:ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica;font-size:16px;}#mermaid-9locys34zsj p{margin:0;}#mermaid-9locys34zsj .entityBox{fill:#1f2020;stroke:#ccc;}#mermaid-9locys34zsj .relationshipLabelBox{fill:hsl(20, 1.5873015873%, 12.3529411765%);opacity:0.7;background-color:hsl(20, 1.5873015873%, 12.3529411765%);}#mermaid-9locys34zsj .relationshipLabelBox rect{opacity:0.5;}#mermaid-9locys34zsj .labelBkg{background-color:rgba(32.0000000001, 31.3333333334, 31.0000000001, 0.5);}#mermaid-9locys34zsj .edgeLabel .label{fill:#ccc;font-size:14px;}#mermaid-9locys34zsj .label{font-family:ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica;color:#ccc;}#mermaid-9locys34zsj .edge-pattern-dashed{stroke-dasharray:8,8;}#mermaid-9locys34zsj .node rect,#mermaid-9locys34zsj .node circle,#mermaid-9locys34zsj .node ellipse,#mermaid-9locys34zsj .node polygon{fill:#1f2020;stroke:#ccc;stroke-width:1px;}#mermaid-9locys34zsj .relationshipLine{stroke:lightgrey;stroke-width:1;fill:none;}#mermaid-9locys34zsj .marker{fill:none!important;stroke:lightgrey!important;stroke-width:1;}#mermaid-9locys34zsj :root{--mermaid-font-family:ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica;}

purchases

shown in

categorizes

hosts

contains

generates

reserved by

User

int

id

PK

string

name

string

email

Ticket

int

id

PK

float

price

ForeignKey

user

ForeignKey

screening

ForeignKey

seat

ForeignKey

movie

ForeignKey

movietheater

Movie

int

id

PK

string

title

int

duration

ForeignKey

genre

Screening

int

id

PK

date

date

time

time

ForeignKey

movie

ForeignKey

movietheater

Genre

int

id

PK

string

name

string

description

MovieTheater

int

number

PK

string

name

string

location

Seat

int

id

PK

int

number

int

row

string

type

ForeignKey

movietheater

### Core Entities 

Entity

Implementation Status

Primary Model Reference

**User**

Configured

`users.apps.UsersConfig`

**Movie**

Implemented

`movies.models.Movie`

**Genre**

Implemented

`movies.models.Genre`

**MovieTheater**

Implemented

`movietheaters.models.MovieTheater`

**Seat**

Implemented

`movietheaters.models.Seat`

**Screening**

Referenced in diagrams

Not yet in visible codebase

**Ticket**

Configured

`tickets.apps.TicketsConfig`

**Sources:** [backend/docs/diagrams/diagramas-cine.drawio1-514](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/docs/diagrams/diagramas-cine.drawio#L1-L514) [backend/main/settings.py41-44](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L41-L44)

* * *

Request Processing Architecture 
-------------------------------------------

The system processes HTTP requests through Django's layered architecture, from middleware through URL routing to views, serializers, and models.

#mermaid-bn8ed90yeh{font-family:ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-bn8ed90yeh .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-bn8ed90yeh .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-bn8ed90yeh .error-icon{fill:#a44141;}#mermaid-bn8ed90yeh .error-text{fill:#ddd;stroke:#ddd;}#mermaid-bn8ed90yeh .edge-thickness-normal{stroke-width:1px;}#mermaid-bn8ed90yeh .edge-thickness-thick{stroke-width:3.5px;}#mermaid-bn8ed90yeh .edge-pattern-solid{stroke-dasharray:0;}#mermaid-bn8ed90yeh .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-bn8ed90yeh .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-bn8ed90yeh .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-bn8ed90yeh .marker{fill:lightgrey;stroke:lightgrey;}#mermaid-bn8ed90yeh .marker.cross{stroke:lightgrey;}#mermaid-bn8ed90yeh svg{font-family:ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica;font-size:16px;}#mermaid-bn8ed90yeh p{margin:0;}#mermaid-bn8ed90yeh .label{font-family:ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica;color:#ccc;}#mermaid-bn8ed90yeh .cluster-label text{fill:#F9FFFE;}#mermaid-bn8ed90yeh .cluster-label span{color:#F9FFFE;}#mermaid-bn8ed90yeh .cluster-label span p{background-color:transparent;}#mermaid-bn8ed90yeh .label text,#mermaid-bn8ed90yeh span{fill:#ccc;color:#ccc;}#mermaid-bn8ed90yeh .node rect,#mermaid-bn8ed90yeh .node circle,#mermaid-bn8ed90yeh .node ellipse,#mermaid-bn8ed90yeh .node polygon,#mermaid-bn8ed90yeh .node path{fill:#1f2020;stroke:#ccc;stroke-width:1px;}#mermaid-bn8ed90yeh .rough-node .label text,#mermaid-bn8ed90yeh .node .label text,#mermaid-bn8ed90yeh .image-shape .label,#mermaid-bn8ed90yeh .icon-shape .label{text-anchor:middle;}#mermaid-bn8ed90yeh .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-bn8ed90yeh .rough-node .label,#mermaid-bn8ed90yeh .node .label,#mermaid-bn8ed90yeh .image-shape .label,#mermaid-bn8ed90yeh .icon-shape .label{text-align:center;}#mermaid-bn8ed90yeh .node.clickable{cursor:pointer;}#mermaid-bn8ed90yeh .root .anchor path{fill:lightgrey!important;stroke-width:0;stroke:lightgrey;}#mermaid-bn8ed90yeh .arrowheadPath{fill:lightgrey;}#mermaid-bn8ed90yeh .edgePath .path{stroke:lightgrey;stroke-width:2.0px;}#mermaid-bn8ed90yeh .flowchart-link{stroke:lightgrey;fill:none;}#mermaid-bn8ed90yeh .edgeLabel{background-color:hsl(0, 0%, 34.4117647059%);text-align:center;}#mermaid-bn8ed90yeh .edgeLabel p{background-color:hsl(0, 0%, 34.4117647059%);}#mermaid-bn8ed90yeh .edgeLabel rect{opacity:0.5;background-color:hsl(0, 0%, 34.4117647059%);fill:hsl(0, 0%, 34.4117647059%);}#mermaid-bn8ed90yeh .labelBkg{background-color:rgba(87.75, 87.75, 87.75, 0.5);}#mermaid-bn8ed90yeh .cluster rect{fill:hsl(180, 1.5873015873%, 28.3529411765%);stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-bn8ed90yeh .cluster text{fill:#F9FFFE;}#mermaid-bn8ed90yeh .cluster span{color:#F9FFFE;}#mermaid-bn8ed90yeh div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica;font-size:12px;background:hsl(20, 1.5873015873%, 12.3529411765%);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-bn8ed90yeh .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-bn8ed90yeh rect.text{fill:none;stroke-width:0;}#mermaid-bn8ed90yeh .icon-shape,#mermaid-bn8ed90yeh .image-shape{background-color:hsl(0, 0%, 34.4117647059%);text-align:center;}#mermaid-bn8ed90yeh .icon-shape p,#mermaid-bn8ed90yeh .image-shape p{background-color:hsl(0, 0%, 34.4117647059%);padding:2px;}#mermaid-bn8ed90yeh .icon-shape rect,#mermaid-bn8ed90yeh .image-shape rect{opacity:0.5;background-color:hsl(0, 0%, 34.4117647059%);fill:hsl(0, 0%, 34.4117647059%);}#mermaid-bn8ed90yeh .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-bn8ed90yeh .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-bn8ed90yeh :root{--mermaid-font-family:ui-sans-serif,-apple-system,system-ui,Segoe UI,Helvetica;}

ORM Models

Data Transformation

View Functions

URL Dispatching

Middleware Pipeline

Application Entry Points

main.wsgi.application

main.asgi.application

SecurityMiddleware

SessionMiddleware

CsrfViewMiddleware

AuthenticationMiddleware

main.urls.urlpatterns

movies.urls

admin.site.urls

movies.views movie\_list movie\_detail add\_movie

movietheaters.views

movies.serializers MovieSerializer GenreSerializer

movietheaters.serializers MovieTheaterSerializer SeatSerializer

movies.models Movie Genre

movietheaters.models MovieTheater Seat

db.sqlite3

### Middleware Configuration 

The request pipeline includes the following middleware in order:

1.  `django.middleware.security.SecurityMiddleware` - Security headers and HTTPS
2.  `django.contrib.sessions.middleware.SessionMiddleware` - Session management
3.  `django.middleware.common.CommonMiddleware` - Common processing
4.  `django.middleware.csrf.CsrfViewMiddleware` - CSRF protection
5.  `django.contrib.auth.middleware.AuthenticationMiddleware` - User authentication
6.  `django.contrib.messages.middleware.MessageMiddleware` - Flash messages
7.  `django.middleware.clickjacking.XFrameOptionsMiddleware` - Clickjacking protection

**Sources:** [backend/main/settings.py47-55](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L47-L55) [backend/main/settings.py57-74](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L57-L74)

* * *

Database Configuration 
----------------------------------

The system uses SQLite as its database backend with the following configuration:

Setting

Value

Reference

**Database Engine**

`django.db.backends.sqlite3`

[backend/main/settings.py82](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L82-L82)

**Database File**

`BASE_DIR / 'db.sqlite3'`

[backend/main/settings.py83](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L83-L83)

**Base Directory**

`Path(__file__).resolve().parent.parent`

[backend/main/settings.py16](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L16-L16)

The database file `db.sqlite3` is located in the `backend` directory at the same level as the `main` package.

**Sources:** [backend/main/settings.py80-85](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L80-L85) [backend/main/settings.py13-16](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L13-L16)

* * *

Application Implementation Status 
---------------------------------------------

The table below shows which domain applications are fully implemented versus configured but not yet visible in the codebase:

Application

Status

Components Available

**movies**

✓ Fully Implemented

models, views, serializers, admin, migrations

**movietheaters**

✓ Fully Implemented

models, views, serializers, admin, migrations

**users**

⚠ Configured Only

Registered in `INSTALLED_APPS`, implementation not visible

**tickets**

⚠ Configured Only

Registered in `INSTALLED_APPS`, implementation not visible

For detailed documentation of implemented applications, see:

*   [Movies Application](#4) - Movie catalog and genre management
*   [MovieTheaters Application](#5) - Theater and seat management
*   [Users and Tickets Applications](#6) - Overview of configured but not yet documented apps

**Sources:** [backend/main/settings.py33-45](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L33-L45)

* * *

Development Configuration 
-------------------------------------

The system is currently configured for development with the following settings:

Setting

Value

Security Note

`DEBUG`

`True`

Not suitable for production

`SECRET_KEY`

Hard-coded in settings

Must be moved to environment variables for production

`ALLOWED_HOSTS`

`[]` (empty)

Must be configured for production deployment

**Sources:** [backend/main/settings.py22-28](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/main/settings.py#L22-L28)

* * *

System Diagrams Reference 
-------------------------------------

The `backend/docs/diagrams/diagramas-cine.drawio` file contains the original conceptual entity-relationship diagrams that informed the system design. These diagrams show:

*   Entity relationships between User, Movie, Ticket, Screening, MovieTheater, and Seat
*   Cardinality constraints (1:1, 1:N, N:M)
*   Database table structures with field types and primary keys

**Sources:** [backend/docs/diagrams/diagramas-cine.drawio1-514](https://github.com/GRMiguelAngel/proyecto-cine/blob/8117f6f4/backend/docs/diagrams/diagramas-cine.drawio#L1-L514)