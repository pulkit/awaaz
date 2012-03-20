google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'hall');
        data.addColumn('number', '');
        data.addRows(9);
        data.setValue(0, 0, 'RK');
        data.setValue(0, 1, 205);

        data.setValue(1, 0, 'RP');
        data.setValue(1, 1, 45);

        data.setValue(2, 0, 'azad');
        data.setValue(2, 1, 250);

        data.setValue(3, 0, 'nehru');
        data.setValue(3, 1, 352.5);

        data.setValue(4, 0, 'patel');
        data.setValue(4, 1, 210);

        data.setValue(5, 0, 'SN');
        data.setValue(5, 1, 37.5);

	    data.setValue(6, 0, 'MS');
        data.setValue(6, 1, 130);

        data.setValue(7, 0, 'LLR');
        data.setValue(7, 1, 195);
        
        data.setValue(8, 0, 'HJB');
        data.setValue(8, 1, 75);

        var chart = new google.visualization.ColumnChart(document.getElementById('GcChart1'));
        chart.draw(data, {width: 300, height: 220, title: '',
                          hAxis: {title: 'Hall', titleTextStyle: {color: 'red'}}
                         });
      }
