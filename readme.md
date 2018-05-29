Sprinkler
===

Temperature: 30, Humidity: 30

Temperature -> (hot, 1)

Humidity -> [(dry, 0.4), (normal, 0.6)]

<table>
    <tr>
        <th>hum, temp</th>
        <th>very cold</th>
        <th>cold</th>
        <th>normal</th>
        <th>warm</th>
        <th>hot</th>
    </tr>
    <tr>
        <td>wet</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>normal</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0.6</td>
    </tr>
    <tr>
        <td>dry</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0.4</td>
    </tr>
<table>

=> short = 0, medium = 0, <b>long = 0.6</b>

long time => <b>(80, 0.6)</b>
