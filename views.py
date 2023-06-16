import numpy as np

def anova_view(request):
    if request.method == 'POST':
        row_count = int(request.POST.get('row_count'))
        column_count = int(request.POST.get('column_count'))
        replication_count = int(request.POST.get('replication_count'))
        
        data = [[[] for j in range(column_count)] for i in range(row_count)]
        for i in range(row_count):
            for j in range(column_count):
                for k in range(replication_count):
                    data[i][j].append(float(request.POST.get(f'X{i+1}{j+1}{k+1}')))
        
"""        
<!DOCTYPE html>


<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <p> {{ column_count }}</p>
  <form method="post" action="values/">
    {% csrf_token %}
    <label for="row_count">Number of Rows:</label>
    <input type="number" name="row_count" id="row_count" value="" min="1" /><br />
    <label for="column_count">Number of Columns:</label>
    <input type="number" name="column_count" id="column_count" value="1" min="1" /><br />
    <label for="replication_count">Number of Replications:</label>
    <input type="number" name="replication_count" id="replication_count" value="1" min="1" /><br />

    <table>
      <thead>
        <tr>
          <th></th>
          {% for j in column_count %}
          <th>Column {{ j}}</th>
          {% endfor %}
        </tr>
      </thead>
      <tbody>
        {% for i in row_count %}
        <tr>
          <th>Row {{ i }}</th>
          {% for j in column_count %}
          <td>
            {% for k in replication_count %}
            <input type="number" name="X{{ i }}{{ j }}{{ k }}" id="X{{ i }}{{ j }}{{ k }}" value="0" /> {% endfor %}
          </td>
          {% endfor %}
        </tr>
        {% endfor %}
      </tbody>
    </table>

    <input type="submit" value="Calculate" />
  </form>
</body>

</html> """