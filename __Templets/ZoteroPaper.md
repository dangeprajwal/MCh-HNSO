---
DOI: "{{DOI}}"
Title: "{{title}}"
Summary: ""
Year: "{{date|year}}"
Journal: "{{journalAbbreviation}}"
---

## [[{{citekey}}.pdf|{{title}}]]

{% for t in tags %}#{{t.tag | replace(' ','-')}} {% endfor %}

> [!Cite]  
> {{bibliography}}

>[!Important]


{% for n in notes %}
{{n.note}}
{% endfor %}

---

#### Annotations

{% for annotation in annotations %}
{% if annotation.annotatedText %}
{% if annotation.colorCategory == "Blue" %}🔵{% endif %}{% if annotation.colorCategory == "Red" %}🔴{% endif %}{% if annotation.colorCategory == "Green" %}🟢{% endif %}{% if annotation.colorCategory == "Yellow" %}🟡{% endif %}{% if annotation.colorCategory == "Gray" %}🌑{% endif %}{% if annotation.colorCategory == "Purple" %}🟣{% endif %}{% if annotation.colorCategory == "Orange" %}🟠{% endif %}{{annotation.annotatedText}}{% endif %}
{% if annotation.imageBaseName %}![[{{annotation.imageBaseName}}]]{% endif %}
{% if annotation.comment %}=={{annotation.comment}}=={% endif %}
{% endfor %}

---