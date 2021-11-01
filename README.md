## About
This is a simple single page application for ordering pizza online. This is not meant for production.


## Blueplan

Frontend
pnpm
vite
svelte

Package manager
frontend framework
Bundler, build tool



Database
Server, Backend


Backend
postgreSQL
python
django

## UML
A very simple UML model for pizza is provided. Essentially, for one pizza, you choose one shape, one sauce, some topping and some seasoning.

<img src="./public/UML_Pizza.svg" alt="UML diagram of a pizza">

Note that, conversely, each ingredient will (likely) appear in multiple pizza. This is not as obvious as it seems. Most often we think the pizza we ordered has an indepedent existence with any other pizza. The issue here is confusion of instance vs class. Although each pizza is separate and indepedent, they are always made of a small set of ingredients.

## Admin page
I have set up a read-only user so that you can login the admin page and have a look inside.

| username    | password       |
|-------------|----------------|
| view_client | enter_pizzeria |

This account cannot modify anything, not even order.

## Technical commentary
<details>
    <ul>
        <li>
            A database is meaningless for a singleton. But under Django framework, it is the easiest way to implment a site-wide setting that allows modifications.
        </li>
    </ul>
</details>