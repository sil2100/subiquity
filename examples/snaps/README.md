## Sample snap data

This directory contains canned responses from snapd's /v2/find endpoint that
can be shown in the SnapList view by passing the --snaps-from-examples flag to
subiquity-tui (instead of waiting on your local snapd and network). It was
generated something like this:

```
$ curl --silent --unix-socket /var/run/snapd.socket a/v2/find?section=server | jq . > find-output.json
$ for x in $(cat find-output.json | jq -r '.result  | .[].name'); do curl --silent --unix-socket /var/run/snapd.socket a/v2/find?name=$x | jq . > info-$x.json; done
```
