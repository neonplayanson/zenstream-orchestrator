"use client";
import { notFound } from "next/navigation";

/**
 * RegEmptyLayout component that triggers a 404 not found error.
 * @returns A React element that triggers a 404 not found error.
 */
export default function RegEmptyLayout() {
  notFound();
}
