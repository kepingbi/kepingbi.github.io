---
title: Students
nav:
  order: 10
  # tooltip: 团队成员
---
# <i class="fas fa-users"></i>Students
## Current

{%
  include list.html
  data="members"
  component="portrait"
  filters="group:current"
%}

{% include section.html %}

## Former

{%
  include list.html
  data="members"
  component="portrait"
  filters="group: former"
%}



{% include section.html %}
