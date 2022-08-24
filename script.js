


const CSV1 =
    "https://raw.githubusercontent.com/dylanmackb9/agatha-text-analysis/main/hosting/Data/freq.csv";

const CSV2 = 
    "https://raw.githubusercontent.com/dylanmackb9/agatha-text-analysis/main/hosting/Data/unique.csv"



function plotFromCSV(dat, divy) {
    d3.csv(dat, function(err, rows) {
        console.log(divy);
        if (divy == "plot1") {
            processData1(rows, divy);

        } else if (divy == "plot2") {
            processData2(rows, divy);
        }
    });
}


function processData1(allRows, divy) {
    let t = [];  // title
    let x = [];  // year
    let y1 = [];  // freq 1-4
    let y2 = [];
    let y3 = [];
    let y4 = [];
    let w1 = [];  // word 1-4
    let w2 = [];
    let w3 = [];
    let w4 = [];
    let row;

    let i = 0;
    while (i < allRows.length) {
        row = allRows[i];
        t.push(row["Title"]);
        x.push(row["Publish Year"]);
        y1.push(row["Frequency1"]);
        y2.push(row["Frequency2"]);
        y3.push(row["Frequency3"]);
        y4.push(row["Frequency4"]);
        w1.push(row["word1"]);
        w2.push(row["Word2"]);
        w3.push(row["Word3"]);
        w4.push(row["Word4"]);
        i += 1;
    }
    
    

    makePlotly1(divy, t, x, y1, y2, y3, y4, w1, w2, w3, w4);
}


function processData2(allRows, divy) {
    let t = [];  // title
    let x = [];  // year
    let y1 = [];  // unique words
    let y2 = [];  // total words
    let y3 = []; // unique / total
    let row;

    let i = 0;
    while (i < allRows.length) {
        row = allRows[i];
        t.push(row["Title"]);
        x.push(row["Publish Year"]);
        y1.push(row["Unique Words"]);
        y2.push(row["Total Words"]);
        y3.push(row["Percent Unique"]);
        i += 1;
    }

    makePlotly2(divy, t, x, y1, y2, y3);

}



function makePlotly1(divy, t, x, y1, y2, y3, y4, w1, w2, w3, w4) {
    let traces = [
        {
            x: x, 
            y: y1,
            mode: 'markers',
            type: 'scatter',
            name: "'something'",
            //line: {color: "#387fba", width: 3}
            text: t,
            marker: { size: 6}
        },
        {
            x: x, 
            y: y2,
            mode: 'markers',
            type: 'scatter',
            name: "'someone'",
            //line: {color: "#387fba", width: 3}
            text: t,
            marker: { size: 6}
        },
        {
            x: x, 
            y: y3,
            mode: 'markers',
            type: 'scatter',
            name: "'anything'",
            //line: {color: "#387fba", width: 3}
            text: t,
            marker: { size: 6}
        },
        {
            x: x, 
            y: y4,
            mode: 'markers',
            type: 'scatter',
            name: "'they'",
            //line: {color: "#387fba", width: 3}
            text: t,
            marker: { size: 6}
        }
    ];


    let layout = {
        title: "Frequency (%) of Indefinite Pronouns in Agatha Christie Novels, 1920-1975",
        yaxis: {
            range: [0, .6],
            title: "% Of Total Words",
        },
        xaxis: {
            title: "Years",
        },
    };



    //https://plot.ly/javascript/configuration-options/
    let config = { 
        responsive: true,
        scrollZoom: true,
        displaylogo: false,
        responsive: true
        // staticPlot: true,
        // editable: true
    };

    Plotly.newPlot(divy, traces, layout, config);
}



function makePlotly2(divy, t, x, y1, y2, y3) {
    let traces = [
        {
            x: x, 
            y: y3,
            mode: 'markers',
            type: 'scatter',
            name: "'something'",
            //line: {color: "#387fba", width: 3}
            text: t,
            marker: { size: 6}
        }
    ];


    let layout = {
        title: "Percent (%) of Total Words Unique in Agatha Christie Novels, 1920-1975",
        yaxis: {
            range: [6, 15],
            title: "% Of Total Words Unique",
        },
        xaxis: {
            title: "Years",
        },
    };



    
    let config = { 
        responsive: true,
        scrollZoom: true,
        displaylogo: false,
        responsive: true
        // staticPlot: true,
        // editable: true
    };

    Plotly.newPlot(divy, traces, layout, config);
}





 plotFromCSV(CSV1, "plot1");
 plotFromCSV(CSV2, "plot2")

















