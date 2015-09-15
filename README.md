# War on Ice API

### Getting Players
```
GET /api/players
```
Get all players, ever.

| parameter | description |
| --------- | ------------|
| page      | Return player information by page. Default is 1 |
| limit     | Limit the number of player records returned. Default is 20 |
| order     | Sort player records. Default is name |

These below are for acceptance, edit and flat out rejection. What will be the
approach to detailing data? Will it be endpoints with many, many `query params`
or providing longer detailed `urls` or a nice balance of both?

```
GET /api/players/ryan-getzlaf
GET /api/teams/new-jersey-devils
GET /api/seasons/2014
GET /api/games
GET /api/games/2015/05/30
GET /api/playoffs/2012
GET /api/goalies
```
