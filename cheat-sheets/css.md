# CSS layout

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr));
  gap: 1rem;
}
:focus-visible { outline: 2px solid currentColor; outline-offset: 3px; }
@media (prefers-reduced-motion: reduce) {
  .animated { animation: none; }
}
```
Use semantic HTML and test responsive layouts with keyboard navigation.

## Official reference

[CSS layout documentation](https://developer.mozilla.org/en-US/docs/Web/CSS)
