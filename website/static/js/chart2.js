google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'hall');
        data.addColumn('number', '');
        data.addRows(7);
        data.setValue(0, 0, 'RK');
        data.setValue(0, 1, 28);

        data.setValue(1, 0, 'RP');
        data.setValue(1, 1, 38);

        data.setValue(2, 0, 'azad');
        data.setValue(2, 1, 17);

        data.setValue(3, 0, 'nehru');
        data.setValue(3, 1, 43);

        data.setValue(4, 0, 'patel');
        data.setValue(4, 1, 42);

        data.setValue(5, 0, 'MS');
        data.setValue(5, 1, 47);

        data.setValue(6, 0, 'LLR');
        data.setValue(6, 1, 28);

        var chart = new google.visualization.ColumnChart(document.getElementById('GcChart2'));
        chart.draw(data, {width: 300, height: 220, title: '',
                          hAxis: {title: 'Hall', titleTextStyle: {color: 'red'}}
                         });
      }
