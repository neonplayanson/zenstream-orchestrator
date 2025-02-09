/**
 * APILayout component that provides the layout for the API pages.
 * @param children - The child components to render inside the layout.
 * @returns A React element containing the API layout.
 */
export default function APILayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
